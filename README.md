to run test cases having tag sanity
behave --tags=sanity

OR:- to run test cases which are either belongs sanity or abcd
behave --tags=sanity,abcd

And:- to run test cases which are either belongs sanity And abcd
behave --tags=sanity --tags=smoke
----------------------------------------------------------------------------------------------
behave -f allure_behave.formatter:AllureFormatter -o C:\Users\harshalashok_warkar\study_codes\bdd_demo
allure generate C:\Users\harshalashok_warkar\study_codes\bdd_demo\report --clean
allure serve C:\Users\harshalashok_warkar\study_codes\bdd_demo\report
----------------------------------------------------------------------------------------------

