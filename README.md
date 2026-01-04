A backend parking slot allocation system that helps drivers find available parking spots and allows parking lot managers to manage space allocation efficiently.
Users can view free slots, reserve a slot, check status and receive confirmation.
Admins can add parking areas, create slots, view reservations and mark slots as occupied or available.


## Endpoints
Base url: http://127.0.0.1:8000/api/

## 1 - Accounts App (Authentication)

### Register User
**POST** `/auth/register/`

**Body (JSON):**
```json
{
  "username": "user_1",
  "email": "user1@example.com",
  "password": "password123"
}
```

 

### Login User
**POST** `/auth/login/`

**Body (JSON):**
```json
{
  "username": "user_1",
  "password": "password123"
}
```

**Response:**
```json
{
  "token": "abc123xyz456"
}
```

  

### Get User Profile
**GET** `/auth/profile/`

**Headers:**
```
Authorization: Token abc123xyz456
```

**Response:**
```json
{
  "user": "user_1",
  "phone_number": "",
  "is_admin": false
}
```
 

## 2 - Parking App

### Create Parking Lot (Admin)
**POST** `/parking-lots/`

**Headers:**
```
Authorization: Token admin_token_here
```

**Body (JSON):**
```json
{
  "name": "Office Parking",
  "location": "Westlands",
  "total_slots": 30
}
```

  

### View All Parking Lots
**GET** `/parking-lots/`

**Headers:**
```
Authorization: Token abc123xyz456
```


### Add Parking Slot to a Lot (Admin)
**POST** `/parking-lots/1/slots/`

**Headers:**
```
Authorization: Token admin_token_here
```

**Body (JSON):**
```json
{
  "slot_number": "A5"
}
```

  

### View Available Parking Slots
**GET** `/slots/available/`

**Headers:**
```
Authorization: Token abc123xyz456
```

**Response:**
```json
[
  {
    "id": 1,
    "slot_number": "A1",
    "status": "available"
  }
]
```

  

## 3 - Booking App (Reservations)

### Create Booking
**POST** `/booking/create/`

**Headers:**
```
Authorization: Token abc123xyz456
```

**Body (JSON):**
```json
{
  "slot_id": 1,
  "start_time": "2025-12-04T10:10:00",
  "end_time": "2025-12-04T12:12:00"
}
```

  

### View My Bookings
**GET** `/booking/my/`

**Headers:**
```
Authorization: Token abc123xyz456
```

  

### Check In (Occupy Slot)
**PUT** `/booking/1/check-in/`

**Headers:**
```
Authorization: Token abc123xyz456
```

  

### Check Out (Free Slot)
**PUT** `/booking/1/check-out/`

**Headers:**
```
Authorization: Token abc123xyz456