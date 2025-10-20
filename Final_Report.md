# Testing Report FlySafair flight booking website

## Executive Summary
This report summarizes the testing activities performed against the FlySafair flight booking flow (search, passenger details, booking summary). Tests were executed according to the Test Plan and Test Cases in this project. The verification focused on functional flows across desktop browsers (Chrome, Edge) and network profiles (3G, 4G, WiFi).

## Scope
In-scope:
- Flight search functionality
- Passenger information entry
- Booking confirmation screen

Out-of-scope:
- Payment processing and payment confirmation

## Test Summary
- Total test cases: 13  
- Executed: 12  
- Passed: 12  
- Failed: 0  
- Skipped: 1 (TC-FR-010 — booking confirmation reference number — out of scope)  

Overall pass rate (executed tests): 100.0%  
Overall pass rate (total tests): 92.31%

## Test Coverage
- Functional coverage: All in-scope flows covered by test cases TC-FR-001 through TC-FR-009 and TC-FR-011 through TC-FR-013.
- Environment coverage: Chrome and Microsoft Edge on Windows desktop; network conditions tested across 3G, 4G, and WiFi as per plan.

## Defects Summary
- Total defects logged: 0 (no open defects recorded against executed test cases)
- Known issues: None reported from executed tests
- Example template available for future bug reports (see Test Plan)

## Key Observations
- Flight search and date selection functioned correctly across tested environments.
- Passenger information validation behavior is consistent and produces appropriate validation messages when required fields are empty.
- Baggage selection and booking summary pages display expected options and data.
- The Enter key navigation and passenger count selection behaved as expected.
- Payment and post-submission confirmation with reference numbers were not executed (out of scope).

## Metrics
- Test execution time: (recorded per session in test logs; refer to test run output)
- Test stability: No intermittent or flaky failures observed during runs.
- Defect density: 0 defects / 12 executed tests = 0.0 defects/test (for executed scope)

## Recommendations / Next Steps
1. Execute out-of-scope payment and confirmation tests (TC-FR-010) before release to production.
2. Add cross-platform mobile testing (iOS/Android) and additional browsers to broaden coverage.
3. Run regression test suite after any change to search, passenger form, or booking summary logic.
4. Automate the executed test cases (if not already automated) and integrate into CI for frequent validation.
5. If future defects arise, use the Bug Report Template in the Test Plan for consistent reporting.

## Conclusion
All in-scope features passed validation with no defects found in the executed tests. Proceed with planned next-phase testing for payment and mobile coverage before final sign-off.

### Attachments:
- Test Plan: Test_Plan.md
- Test Cases: Test_cases.md