# IT 3380 Final Project
# by Brandon Buttlar, BJBZRC
import mysql.connector


def print_menu():
    print("")
    print("Choose an option")
    print("------------------------------")
    print("---------- VIEW DATA ---------")
    print("1. View employees data per region")
    print("2. View manager count by department")
    print("3. View dependent data per department")
    print("4. View hiring data by year")
    print("5. View Salary data by department")
    print("6. View Salary data by job title")
    print("7. View dependent data by employee")
    print("8. View location data by country")
    print('')
    print("---------- ADD DATA ----------")
    print("9.  Add new dependent")
    print("10. Add a job")
    print('')
    print("--------- DELETE DATA --------")
    print("11. Delete an employee")
    print("12. Delete a dependent")
    print('')
    print("--------- UPDATE DATA --------")
    print("13. Update employee first name")
    print("14. Update employee last name")
    print("15. Update job minimum salary")
    print("16. Update job maximum salary")
    print('')
    print("------------- EXIT -----------")
    print("17. Exit Application")
    print('')


def get_user_choice():
    print_menu()
    choice = int(input("Enter Choice: "))
    return choice


def query_one_all(mycursor):
    sql_query = 'SELECT * FROM EmployeesPerRegion;'
    mycursor.execute(sql_query)
    query_result = mycursor.fetchall()
    print('')
    for record in query_result:
        print(f"Region: {record[0]} | Employees: {record[1]}")


def query_one_region(mycursor, region):
    sql_query = 'SELECT * FROM EmployeesPerRegion WHERE region_name = %s;'
    mycursor.execute(sql_query, (region,))
    query_result = mycursor.fetchall()
    print('')
    for record in query_result:
        print(f"Region: {record[0]} | Employees: {record[1]}")


def query_two_all(mycursor):
    sql_query = '''SELECT department_name, COUNT(department_name) AS "Number of Managers"
                    FROM managers
                    GROUP BY department_name
                    ORDER BY COUNT(department_name) DESC;'''
    mycursor.execute(sql_query)
    query_result = mycursor.fetchall()
    print("\nDepartment | Number of managers")
    for record in query_result:
        print(f"{record[0]} | {record[1]}")


def query_two_department(mycursor, department):
    sql_query = '''SELECT department_name, COUNT(department_name) AS "Number of Managers"
                    FROM managers
                    WHERE department_name = %s
                    GROUP BY department_name
                    ORDER BY COUNT(department_name) DESC;'''
    mycursor.execute(sql_query, (department,))
    query_result = mycursor.fetchall()
    print("\nDepartment | Number of managers")
    for record in query_result:
        print(f"{record[0]} | {record[1]}")


def query_three_all(mycursor):
    sql_query = 'SELECT * FROM DependentsByDepartment;'
    mycursor.execute(sql_query)
    query_result = mycursor.fetchall()
    print('')
    for record in query_result:
        print(f"Department: {record[0]} | Dependents: {record[1]}")


def query_three_dept(mycursor, department):
    sql_query = '''SELECT *
                    FROM DependentsByDepartment
                    WHERE department_name = %s;'''
    mycursor.execute(sql_query, (department,))
    query_result = mycursor.fetchall()
    print('')
    for record in query_result:
        print(f"Department: {record[0]} | Dependents: {record[1]}")


def query_four_all(mycursor):
    sql_query = 'SELECT * FROM HiresByYear;'
    mycursor.execute(sql_query)
    query_result = mycursor.fetchall()
    print('')
    for record in query_result:
        print(f"Year: {record[0]} | Employees Hired: {record[1]}")


def query_four_year(mycursor, year):
    sql_query = 'SELECT * FROM HiresByYear WHERE year = %s;'
    mycursor.execute(sql_query, (year,))
    query_result = mycursor.fetchall()
    print('')
    for record in query_result:
        print(f"Year: {record[0]} | Employees Hired: {record[1]}")


def query_five_all(mycursor):
    sql_query = 'SELECT * FROM SalaryByDepartment;'
    mycursor.execute(sql_query)
    query_result = mycursor.fetchall()
    print('')
    for record in query_result:
        print(f"Department: {record[0]} | Salary: ${record[1]}")


def query_five_dept(mycursor, department):
    sql_query = 'SELECT * FROM SalaryByDepartment WHERE department_name = %s;'
    mycursor.execute(sql_query, (department,))
    query_result = mycursor.fetchall()
    print('')
    for record in query_result:
        print(f"Department: {record[0]} | Salary: ${record[1]}")


def query_six_all(mycursor):
    sql_query = 'SELECT * FROM SalaryByJobTitle;'
    mycursor.execute(sql_query)
    query_result = mycursor.fetchall()
    print('')
    for record in query_result:
        print(f"Job Title: {record[0]} | Salary: ${record[1]}")


def query_six_title(mycursor, title):
    sql_query = '''SELECT *
                    FROM SalaryByJobTitle
                    WHERE job_title = %s;'''
    mycursor.execute(sql_query, (title,))
    query_result = mycursor.fetchall()
    print('')
    for record in query_result:
        print(f"Job Title: {record[0]} | Salary: ${record[1]}")


def query_seven_all(mycursor):
    sql_query = 'SELECT * FROM EmployeeDependents;'
    mycursor.execute(sql_query)
    query_result = mycursor.fetchall()
    print("\nEmployees and their dependents:")
    print('')
    for record in query_result:
        print(f"{record[0]} {record[1]}, {record[2]}, {record[3]}, Dependents: {record[4]}")


def query_seven_employee(mycursor, employee):
    sql_query = 'SELECT * FROM EmployeeDependents WHERE first_name = %s;'
    mycursor.execute(sql_query, (employee,))
    query_result = mycursor.fetchall()
    print("\nEmployee's dependents:")
    for record in query_result:
        print(f"{record[0]} {record[1]}, {record[2]}, {record[3]}, Dependents: {record[4]}")


def query_eight_all(mycursor):
    sql_query = 'SELECT * FROM CountryLocation;'
    mycursor.execute(sql_query)
    query_result = mycursor.fetchall()
    print('')
    for record in query_result:
        print(f"Country: {record[0]} | Number of Offices: {record[1]}")


def query_eight_country(mycursor, country):
    sql_query = 'SELECT * FROM CountryLocation WHERE country_name = %s;'
    mycursor.execute(sql_query, (country,))
    query_result = mycursor.fetchall()
    print('')
    for record in query_result:
        print(f"Country: {record[0]} | Number of Offices: {record[1]}")


def add_dependents(mycursor, mydb, dependent_id, first_name, last_name, relationship, employee_id):
    sqlquery = '''INSERT INTO dependents (dependent_id, first_name, last_name, relationship, employee_id)
                  VALUES (%s, %s, %s, %s, %s);'''
    mycursor.execute(sqlquery, (dependent_id, first_name, last_name, relationship, employee_id))
    mydb.commit()
    print(f"\nDependent {first_name} {last_name} added to database")


def add_job(mycursor, mydb, job_id, job_title, min_salary, max_salary):
    sqlquery = '''INSERT INTO jobs (job_id, job_title, min_salary, max_salary)
                  VALUES (%s, %s, %s, %s);'''
    mycursor.execute(sqlquery, (job_id, job_title, min_salary, max_salary))
    mydb.commit()
    print(f"\nJob {job_title} added to database")


def delete_employee(mycursor, mydb, employee_id):
    try:
        sqlquery = 'DELETE FROM employees WHERE employee_id = %s'
        mycursor.execute(sqlquery, (employee_id,))
        mydb.commit()
        print(f"\nEmployee {employee_id} has been deleted")
    except Exception as e:
        print("\nError deleting employee, returning to menu")


def delete_dependent(mycursor, mydb, dependent_id):
    try:
        sqlquery = 'DELETE FROM dependents WHERE dependent_id = %s'
        mycursor.execute(sqlquery, (dependent_id,))
        mydb.commit()
        print(f"\nDependent {dependent_id} has been deleted")
    except Exception as e:
        print("\nError deleting dependent, returning to menu")


def update_first_name(mycursor, mydb, first_name, employee_id):
    sqlquery = 'UPDATE employees SET first_name = %s WHERE employee_id = %s;'
    mycursor.execute(sqlquery, (first_name, employee_id))
    mydb.commit()
    print(f"\nEmployee {employee_id}'s first name has been updated to {first_name}")


def update_last_name_data(mycursor, mydb, employee_id, last_name):
    sqlquery = 'UPDATE employees SET last_name = %s WHERE employee_id = %s;'
    mycursor.execute(sqlquery, (last_name, employee_id))
    mydb.commit()
    print(f"\nEmployee {employee_id}'s last name has been updated to {last_name}")


def update_min_salary(mycursor, mydb, job_title, min_salary):
    sqlquery = 'UPDATE jobs SET min_salary = %s WHERE job_title = %s;'
    mycursor.execute(sqlquery, (min_salary, job_title))
    mydb.commit()
    print(f"\n{job_title}'s minimum salary has been changed")


def update_max_salary(mycursor, mydb, job_title, max_salary):
    sqlquery = 'UPDATE jobs SET max_salary = %s WHERE job_title = %s;'
    mycursor.execute(sqlquery, (max_salary, job_title))
    mydb.commit()
    print(f"\n{job_title}'s maximum salary has been changed")


def main():
    try:
        mydb = mysql.connector.connect(
            host="mysql-container",
            user="root",
            passwd="root",
            database="project2"
        )
        print("\nSuccessfully connected to the HR database!")
    except Exception as e:
        print(f"\nError: {e}\nExiting program...\n")
        quit()
    mycursor = mydb.cursor()

    while(True):
        try:
            user_choice = get_user_choice()
        except Exception as e:
            print("\nError: Please enter a number between 1 and 17")
            continue

        try:
            if user_choice == 1:
                view_all = input("Do you want to view all data? (y/n): ")
                if view_all.lower() == "y":
                    query_one_all(mycursor)
                elif view_all.lower() == "n":
                    region = input("Enter region: ")
                    query_one_region(mycursor, region)
                else:
                    print("Invalid input, please try again")
                    continue

            elif user_choice == 2:
                view_all = input("Do you want to view all data? (y/n): ")
                if view_all.lower() == "y":
                    query_two_all(mycursor)
                elif view_all.lower() == "n":
                    department = input("Enter department: ")
                    query_two_department(mycursor, department)
                else:
                    print("Invalid input, please try again")
                    continue

            elif user_choice == 3:
                view_all = input("Do you want to view all data? (y/n): ")
                if view_all.lower() == "y":
                    query_three_all(mycursor)
                elif view_all.lower() == "n":
                    department = input("Enter department: ")
                    query_three_dept(mycursor, department)
                else:
                    print("Invalid input, please try again")
                    continue

            elif user_choice == 4:
                view_all = input("Do you want to view all data? (y/n): ")
                if view_all.lower() == "y":
                    query_four_all(mycursor)
                elif view_all.lower() == "n":
                    year = input("Enter a year: ")
                    query_four_year(mycursor, year)
                else:
                    print("Invalid input, please try again")
                    continue

            elif user_choice == 5:
                view_all = input("Do you want to view all data? (y/n): ")
                if view_all.lower() == "y":
                    query_five_all(mycursor)
                elif view_all.lower() == "n":
                    department = input("Enter department: ")
                    query_five_dept(mycursor, department)
                else:
                    print("Invalid input, please try again")
                    continue
                    
            elif user_choice == 6:
                view_all = input("Do you want to view all data? (y/n): ")
                if view_all.lower() == "y":
                    query_six_all(mycursor)
                elif view_all.lower() == "n":
                    title = input("Enter job title: ")
                    query_six_title(mycursor, title)
                else:
                    print("Invalid input, please try again")
                    continue

            elif user_choice == 7:
                view_all = input("Do you want to view all data? (y/n): ")
                if view_all.lower() == "y":
                    query_seven_all(mycursor)
                elif view_all.lower() == "n":
                    employee = input("Enter employee's first name: ")
                    query_seven_employee(mycursor, employee)
                else:
                    print("Invalid input, please try again")
                    continue

            elif user_choice == 8:
                view_all = input("Do you want to view all data? (y/n): ")
                if view_all.lower() == "y":
                    query_eight_all(mycursor)
                elif view_all.lower() == "n":
                    country = input("Enter country: ")
                    query_eight_country(mycursor, country)
                else:
                    print("Invalid input, please try again")
                    continue
            
            elif user_choice == 9:
                dependent_id = input("Enter dependent id: ")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                relationship = input("Enter relationship: ")
                employee_id = input("Enter employee ID: ")
                add_dependents(mycursor, mydb, dependent_id, first_name, last_name, relationship, employee_id)

            elif user_choice == 10:
                job_id = input("Enter job id: ")
                job_title = input("Enter job title: ")
                min_salary = input("Enter minimum salary: ")
                max_salary = input("Enter maximum salary: ")
                add_job(mycursor, mydb, job_id, job_title, min_salary, max_salary)
            
            elif user_choice == 11:
                employee_id = input("Enter employee id: ")
                delete_employee(mycursor, mydb, employee_id)
            
            elif user_choice == 12:
                dependent_id = input("Enter dependent id: ")
                delete_dependent(mycursor, mydb, dependent_id)

            elif user_choice == 13:
                employee_id = input("Enter employee id: ")
                first_name = input("Enter new first name: ")
                update_first_name(mycursor, mydb, first_name, employee_id)

            elif user_choice == 14:
                employee_id = input("Enter employee id: ")
                last_name = input("Enter new last name: ")
                update_last_name_data(mycursor, mydb, employee_id, last_name)

            elif user_choice == 15:
                job_title = input("Enter job title: ")
                min_salary = input("Enter new minimum salary: ")
                update_min_salary(mycursor, mydb, job_title, min_salary)

            elif user_choice == 16:
                job_title = input("Enter job title: ")
                max_salary = input("Enter new maximum salary: ")
                update_max_salary(mycursor, mydb, job_title, max_salary)

            elif user_choice == 17:
                print("\nGoodbye\n")
                break

            else:
                print("\nError: Please enter a number between 1 and 17")

        except Exception as e:
            print("\nAn error has occurred, please try again")


main()
