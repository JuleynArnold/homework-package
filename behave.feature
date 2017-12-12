Feature: Testing Calc Module

  Scenario: single digit number parse
    Given a test is written
    Then lets parse these single digit numbers
      | number |
      | 0      |
      | 1      |
      | 2      |
      | 3      |
      | 4      |
      | 5      |
      | 6      |
      | 7      |
      | 8      |
      | 9      |

  Scenario: whole number parse
    Given a test is written
    Then lets parse these positive whole numbers
      | number |
      | 1      |
      | 100    |
      | 100000 |
      | 124809214     |
      | 821944014122      |
      | 5395783105175091      |
      | 9223372036854775807      |

  Scenario: floating point number parse
    Given a test is written
    Then lets parse these positive floating point numbers
      | number |
      | 1.0      |
      | 1.01    |
      | 1.0123 |
      | 213.124     |
      | 53215.21124      |

  Scenario: single digit hexadecimal number
    Given a test is written
    Then lets parse these positive single digit hexadecimal numbers
      | number |
      | 0      |
      | 1      |
      | 2      |
      | 3      |
      | 4      |
      | 5      |
      | 6      |
      | 7      |
      | 8      |
      | 9      |
      | A      |
      | B      |
      | C      |
      | D      |
      | E      |
      | F      |

  Scenario: single digit number parse
    Given a test is written
    Then lets parse all combinations of positive hexadecimal numbers
      | number |
      | 0      |
      | 1      |
      | 2      |
      | 3      |
      | 4      |
      | 5      |
      | 6      |
      | 7      |
      | 8      |
      | 9      |
      | A      |
      | B      |
      | C      |
      | D      |
      | E      |
      | F      |

  Scenario: Evaluate system
    Given a test is written
    Then lets evaluate the entire system
      | number |
      | -10000      |
      | -124809214      |
      | -821944014122      |
      | -1.0123      |
      | -213.124      |
      | -53215.21124      |
      | 0x01      |
      | 0x0A      |
      | 0xAF      |
      | 0xC4      |
      | 0xF9     |
