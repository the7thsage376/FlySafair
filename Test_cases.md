# FlySafair Flight Booking System Test Cases

## Flight search test cases

### TC-FR-001: Verify user can select departure and arrival cities
**Preconditions**: User is on FlySafair homepage
**Steps to Reproduce**:
1. Click departure city dropdown
2. Select desired departure city
3. Click arrival city dropdown
4. Select desired arrival city
**Expected Results**: User successfully selects valid departure and arrival cities
**Actual Results**: User can select departure and arrival cities as expected
**Priority**: Very High
**Status**: Passed

### TC-FR-002: Verify user can choose departure and return dates
**Preconditions**: User is on FlySafair homepage
**Steps to Reproduce**:
1. Click departure date field
2. Select valid departure date from calendar
3. Click return date field
4. Select valid return date from calendar
**Expected Results**: User successfully selects valid travel dates
**Actual Results**: User can select departure and return dates as expected
**Priority**: Very High
**Status**: Passed

### TC-FR-003: Verify user can specify number of passengers
**Preconditions**: User is on FlySafair homepage
**Steps to Reproduce**:
1. Click passenger selection dropdown
2. Adjust number of Adult passengers 
3. Adjust number of Child passengers
4. Adjust number of Infant passengers
**Expected Results**: User successfully specifies passenger count for each category
**Actual Results**: User can select passenger numbers as expected
**Priority**: Very High
**Status**: Passed

### TC-FR-004: Verify System displays available flights with pricing
**Preconditions**: 
1. User is on FlySafair homepage
2. Valid route and dates are selected
3. Passenger count is specified

**Steps to Reproduce**:
1. Select departure and arrival cities
2. Select travel dates
3. Specify passenger count
4. Click "Let's go" button
**Expected Results**: System displays available flights with correct pricing for all fare classes
**Actual Results**: Available flights and pricing displayed correctly
**Priority**: Very High
**Status**: Passed

## Passenger Details Test Cases

### TC-FR-005: Verify user can enter passenger information
**Preconditions**: User is on passenger details page
**Steps to Reproduce**:
1. Enter first name in required field
2. Enter last name in required field
3. Enter valid ID/passport number
**Expected Results**: System accepts valid passenger information
**Actual Results**: User can enter passenger details successfully
**Priority**: Very High
**Status**: Passed

### TC-FR-006: Verify user can select baggage options
**Preconditions**: User is on baggage selection page
**Steps to Reproduce**:
1. View available baggage options
2. Select desired checked baggage allowance
3. Add extra baggage if needed
**Expected Results**: User can select and modify baggage options
**Actual Results**: Baggage selection works as expected
**Priority**: High
**Status**: Passed

### TC-FR-007: Verify system validates required fields
**Preconditions**: User is on passenger details page
**Steps to Reproduce**:
1. Leave required fields empty
2. Attempt to proceed to next step
**Expected Results**: System displays validation errors for empty required fields
**Actual Results**: System correctly shows validation errors for empty fields
**Priority**: High
**Status**: Passed

## Booking Confirmation Test Cases

### TC-FR-008: Verify system displays booking summary
**Preconditions**: User has entered all required information
**Steps to Reproduce**:
1. Complete passenger details
2. Navigate to booking summary page
**Expected Results**: System displays accurate booking summary with all details
**Actual Results**: Booking summary displays all entered information accurately
**Priority**: High
**Status**: Passed

### TC-FR-009: Verify user can confirm and submit booking
**Preconditions**: User is on booking summary page
**Steps to Reproduce**:
1. Review booking details
2. Accept terms and conditions
3. Click confirm booking button
**Expected Results**: Booking is successfully submitted
**Actual Results**: Booking submission completes successfully
**Priority**: High
**Status**: Passed

### TC-FR-010: Verify system shows confirmation message and reference number
**Preconditions**: Booking has been submitted
**Steps to Reproduce**:
1. Submit valid booking
2. Wait for confirmation page
**Expected Results**: System displays booking confirmation with reference number
**Actual Results**: Test not executed as feature is out of scope
**Priority**: High
**Status**: Skipped(Out of scope)

## Error Handling Test Cases

### TC-FR-011: Verify system shows error for missing required fields
**Preconditions**: User is on any booking form page
**Steps to Reproduce**:
1. Leave mandatory fields empty
2. Attempt to proceed
**Expected Results**: System displays appropriate error messages
**Actual Results**: Error messages displayed correctly for all missing fields
**Priority**: High
**Status**: Passed

### TC-FR-012: Verify system prevents booking with invalid dates or passenger info
**Preconditions**: User is entering booking details
**Steps to Reproduce**:
1. Enter invalid dates (past dates/incorrect format)
2. Enter invalid passenger information
3. Attempt to proceed
**Expected Results**: System prevents booking and shows validation errors
**Actual Results**: System successfully prevents invalid bookings with clear error messages
**Priority**: High
**Status**: Passed

### TC-FR-013: Verify system handles unavailable flights gracefully
**Preconditions**: Search for a fully booked flight
**Steps to Reproduce**:
1. Select a route and date with no availability
2. Attempt to search
**Expected Results**: System displays appropriate "no flights available" message
**Actual Results**: System shows clear message when no flights are available
**Priority**: Medium
**Status**: Passed

---