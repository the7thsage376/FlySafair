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

**Title**: Login with Invalid Credentials Shows No Feedback
**Description**: Logging in with invalid credentials does not give an Error message and instead resets the form.
**Environment**: Chrome Desktop
**Steps to Reproduce**:  
1. Go to login page  
2. Enter invalid credentials 
3. Click Login 

**Expected**: A clear error message appears  
**Actual**: Nothing happens, and the form resets  
**Severity**: Major 
**Priority**: High

End of test plan

