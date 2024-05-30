import pytest


@pytest.mark.asyncio
async def test_model_transactions(loaded_database_and_model):
    db, Employees = loaded_database_and_model


    """
    Remove the nth and nth-1 emplyees from thge list, and in the same txnm,
    store them aagain.
    and validate outside the txn, that
    """

    async with db as conn:
        async with conn.transaction() as t:
            t.start()
            all_employees = await Employees.all()

            await all_employees[-1].delete()
            await all_employees[-2].delete()


            print(f"--------------- 1 - 2nd last Employee in txn\n\t" + str(all_employees[-2]))

            employee = await all_employees[-1].insert()

            result = await all_employees[-2].save()

            print(f"--------------- 2 - 2nd last Employee in txn after save\n\t" + str(all_employees[-2]))
            t.commit()


    print(f"--------------- 3 - 2nd last Employee out of txn\n\t" + str(all_employees[-2]))
    expect = await Employees.get(
        employee_id=all_employees[-2].employee_id
    )

    print(f"--------------- 4 - 2nd last Employee by ID loaded\n\t" + str(expect))
    assert all_employees[-2] == expect

    # test unique
    try:
        employee = await all_employees[-1].insert()
    except Exception:
        pass
    else:
        assert (
            False
        ), "expected IntegrityError due to duplicate primary key insert attempts"

    new_employee = all_employees[-1]
    new_employee.employee_id = "special"

    async with db:
        await new_employee.insert()

        verify_examples = await Employees.filter(employee_id="special")

    assert len(verify_examples) == 1
