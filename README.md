# Country List Project

[![Backend Tests](https://github.com/broden-wanner/country-list-project/actions/workflows/backend-tests.yml/badge.svg)](https://github.com/broden-wanner/country-list-project/actions/workflows/backend-tests.yml)
[![codecov](https://codecov.io/gh/broden-wanner/country-list-project/branch/main/graph/badge.svg?token=QedVU7QwJb)](https://codecov.io/gh/broden-wanner/country-list-project)

---

**API Root**: [https://countrylist.brodenwanner.com](https://countrylist.brodenwanner.com)

**API Docs**: [https://countrylist.brodenwanner.com/redoc](https://countrylist.brodenwanner.com/redoc)

**Documentation**: [https://countrylist.brodenwanner.com/dev/docs/](https://countrylist.brodenwanner.com/dev/docs/)

---

This project is an application that receives a three-letter code for a North American Country and returns a list of 
all countries a driver must travel through to go from the United State of America to the destination. We 
use a simplified map of North America:
- CAN - Canada borders the United States
- USA - The United States borders Canada and Mexico
- MEX - Mexico borders the United States, Guatemala, and Belize
- BLZ - Belize borders Mexico and Guatemala
- GTM - Guatemala borders Mexico, Belize, El Salvador, and Honduras
- SLV - El Salvador borders Guatemala and Honduras
- HND - Honduras borders Guatemala, El Salvador, and Nicaragua
- NIC - Nicaragua borders Honduras and Costa Rica
- CRI - Costa Rica borders Nicaragua and Panama 
- PAN - Panama borders Costa Rica

<img alt="Simplified North America" src="/docs/img/simplified-north-america-map.png" width="25%">

For instance, sending a GET request to 
`countrylist.brodenwanner.com/PAN` will result in the
following response

```json
{
    "destination": "PAN",
    "list": ["USA", "MEX", "GTM", "HND", "NIC", "CRI", "PAN"]
}
```