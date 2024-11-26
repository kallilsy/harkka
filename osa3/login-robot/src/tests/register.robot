*** Settings ***
Library           AppLibrary

*** Test Cases ***
Register With Valid Username And Password
    Create User       validuser      Strong123
    Output Should Contain    User registered successfully

Register With Already Taken Username And Valid Password
    Create User       existinguser     InitialPass1!
    Create User       existinguser     Strong123
    Output Should Contain    Username is already taken

Registration Fails With Short Username
    Create User       ab      Strong123
    Output Should Contain    Username must be at least 3 characters long and contain only lowercase letters a-z

Register With Enough Long But Invalid Username And Valid Password
    Create User       Invalid1Name     Strong123
    Output Should Contain    Username must be at least 3 characters long and contain only lowercase letters a-z

Register With Valid Username And Too Short Password
    [Documentation]   Testaa, että heikolla salasanalla rekisteröinti epäonnistuu.
    Create User       validuser      only
    Output Should Contain    Password must be at least 8 characters long and contain at least one non-alphabetic character

Register With Valid Username And Long Enough Password Containing Only Letters
    [Documentation]   Testaa, että heikolla salasanalla rekisteröinti epäonnistuu.
    Create User       validuser      onlyletters
    Output Should Contain    Password must be at least 8 characters long and contain at least one non-alphabetic character

