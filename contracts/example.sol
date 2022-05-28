// SPDX-License-Identifier: UNLICENSED
pragma solidity >0.8.0;
// contract Greeter {
//     string public greeting;
//     constructor() public {
//         greeting = 'Hello';
//     }
//     function setGreeting(string memory) public {
//         greeting = _greeting;
//     }
//     function greet() view public returns (string memory) {
//         return greeting;
//     }
// }
contract Person {
    // string[][] public names;
    int  public birthDate;
    int  public deathDate;
    int  public marriageDate;

    Person public spouse;

    constructor() {
        // names = [["Unknown"]];
        birthDate = 0;
        deathDate = 0;
        marriageDate = 0;
    }
    function setBirthDate(int  _unix_timestamp) public {
        birthDate = _unix_timestamp;
    }
    function setDeathDate(int  _unix_timestamp) public {
        birthDate = _unix_timestamp;
    }
    function setMarriageDate(int  _unix_timestamp) public {
        birthDate = _unix_timestamp;
    }
    function setSpouse(Person _spouse) public {
        spouse = _spouse;
    }
}