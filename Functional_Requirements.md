# ✈️ Functional Requirements – FlySafair Automation

This document outlines the expected functional behavior of a flight booking website, based on typical user interactions and industry standards. These requirements guide the scope of automated UI testing.

---

##  Flight Search

- **FR-001**: User can select departure and arrival cities
- **FR-002**: User can choose departure and return dates
- **FR-003**: User can specify number of passengers
- **FR-004**: System displays available flights with pricing

---

## Passenger Details

- **FR-005**: User can enter first name, last name, and ID/passport number
- **FR-006**: User can select baggage options
- **FR-007**: System validates required fields

---

## 🧾 Booking Confirmation

- **FR-008**: System displays booking summary
- **FR-009**: User can confirm and submit booking
- **FR-010**: System shows confirmation message and reference number

---

## 🚫 Error Handling

- **FR-011**: System shows error for missing required fields
- **FR-012**: System prevents booking with invalid dates or passenger info
- **FR-013**: System handles unavailable flights gracefully

---

## 🧪 Test Coverage Mapping

These requirements are covered by the following automated test cases:

- `test_search_valid_inputs.py` → FR-001 to FR-004
- `test_booking_flow.py` → FR-005 to FR-010
- `test_invalid_passenger_data.py` → FR-011 to FR-013