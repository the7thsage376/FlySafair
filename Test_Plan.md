# Test Plan: Flysafair Flight Booking

---
# Scope and Objectives:

## Objectives:

Verify that:

- Users can successfully search for flights by selecting departure and destination locations
- Users can accurately input and save passenger details
- Users can review and complete their flight booking confirmation
- Users can correctly specify the number of adult and child passengers
- Users can navigate forms using keyboard Enter key functionality

---

## In-Scope:

1.  Flight search functionality
2.  Passenger information entry
3.  Booking confirmation screen


## Out of Scope:
- Flight payment confirmation

---


## Tools & Frameworks

- Selenium webdriver with Python
- Python OOP structure
- Pytest

---
### Test Environments

The test environment remained consistent throughout the testing process.

- Browsers: Chrome, Microsoft Edge
- Devices: Desktop (Windows)
- Network conditions: 3G, 4G, WiFi

---
## Bug Report Template

**Title**:
**Preconditions**:
**Steps to Reproduce**:  
**Expected Result**: 
**Actual Result**:  
**Priority**:

## Test Results (Summary)

Based on the executed test cases and the Final Report, the following results were recorded:

- Total test cases: 13
- Executed: 12
- Passed: 12
- Failed: 0
- Skipped: 1 (TC-FR-010 — booking confirmation reference number — out of scope)

Overall pass rate (executed tests): 100.0%
Overall pass rate (total tests): 92.31%

## Metrics

- Test execution time: recorded per session in test logs (refer to test run output)
- Test stability: No intermittent or flaky failures observed during runs
- Defect density: 0 defects / 12 executed tests = 0.0 defects/test (for executed scope)

## Defects Summary

- Total defects logged: 0 (no open defects recorded against executed test cases)
- Known issues: None reported from executed tests

## Key Observations

- Flight search and date selection functioned correctly across tested environments (Chrome, Edge on Windows).
- Passenger information validation behavior is consistent and produces appropriate validation messages when required fields are empty.
- Baggage selection and booking summary pages display expected options and data.
- The Enter key navigation and passenger count selection behaved as expected.
- Payment and post-submission confirmation with reference numbers were not executed (out of scope).

## Recommendations / Next Steps

1. Execute out-of-scope payment and confirmation tests (TC-FR-010) before release to production.
2. Add cross-platform mobile testing (iOS/Android) and additional browsers to broaden coverage.
3. Run regression test suite after any change to search, passenger form, or booking summary logic.
4. Automate the executed test cases (if not already automated) and integrate into CI for frequent validation.
5. If future defects arise, use the Bug Report Template in the Test Plan for consistent reporting.

## Conclusion

All in-scope features passed validation with no defects found in the executed tests. Proceed with planned next-phase testing for payment and mobile coverage before final sign-off.


