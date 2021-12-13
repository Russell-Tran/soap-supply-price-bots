// REPLACE CONSTANTS HERE
let fantastic_engine_url = 'https://webhook.site/e37c60c1-ac26-4c6c-b60f-35c8414f5cb1';
let fantastic_engine_apikey = '';

// ==========

let inputConfig = input.config();
let product_url = inputConfig.product_url;
let record_id = inputConfig.record_id;
let table = base.getTable("aarontable1");

let response = await fetch(fantastic_engine_url, {
    method: 'POST',
    body: JSON.stringify({
        'url' : product_url,
        "shipping_address" : {
            "first_name" : "John",
            "last_name" : "Snow",
            "email" : "winteriscoming@gmail.com",
            "phone" : "(949) 361-8200",
            "fax" : "(949) 493-8729",
            "company" : "Cool Soap, Inc.",
            "address" : "15 Calle Loyola",
            "address_2" : "Suite #15",
            "city" : "San Clemente",
            "state" : "California",
            "country" : "United States",
            "zipcode" : "92673"
        }
    }),
    headers: {
        'Content-Type': 'application/json',
    },
});

await table.updateRecordAsync(record_id, {
    "subtotal": "$4.50",
    "shipping" : "$0.50",
    "total" : "$5.00"
});

//console.log(await response.json());
await response;