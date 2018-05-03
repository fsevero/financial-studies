## Databases

Description of the used databases.

Before knowing more about the datasets, data formats and acceptable performances, I'll make a basic strucure to hold it using the AWS DynamoDB.


[Back to README](/README.md)

## Dataset A

```javascript
{
  // person document number - the main key
  Key: '00000000000',
  Name: 'Fabrício Severo de Severo',
  // Maybe an object with city, state, street, but I'll keep simple by now
  Address: 'Santa Maria - RS',
  Debts: [
    {
      Description: 'List of person debts',
      // $123.45 but as integer to avoid data truncation and conversion errors
      Value: 12345,
      Expiration: '2018-12-31',
      Entity: 'Bank Name'
    }
  ]
}
```

## Dataset B

```javascript
{
  // person document number - the main key
  Key: '00000000000',
  Age: 29,
  // Maybe an object with city, state, street, but I'll keep simple by now
  Address: 'Santa Maria - RS',
  Assets: [
    {
      Description: 'House somwhere',
      // $123,456.78 but as integer to avoid data truncation and conversion errors
      Value: 12345678,
      AcquiredDate: '2017-01-01',
    }
  ],
  Income: [
    {
      Description: 'Main Salary at ...',
      Value: 100000
    }
  ]
}
```

## Dataset C

```javascript
{
  // person document number - the main key
  Key: '00000000000',
  LastSearch: {
    Entity: 'Bank Name',
    Datetime: '2018-05-01',
  },
  Movements: [
    {
      Entity: 'Shopping',
      Datetime: '2018-05-03 12:30:00',
      // $50.00 but as integer to avoid data truncation and conversion errors
      Value: 5000,
    }
  ],
  // Last use of credit card
  LastCC: {
    Entity: 'Market',
    Datetime: '2018-05-01 19:00:00',
    // $50.00 but as integer to avoid data truncation and conversion errors
    Value: 5000,
  },
}
```

---
[Back to README](/README.md)