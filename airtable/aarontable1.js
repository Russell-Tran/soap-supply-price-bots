// REPLACE CONSTANTS HERE
let fantastic_engine_url = '';
let fantastic_engine_apikey = '';

// ==========

let inputConfig = input.config();
let product_url = inputConfig.product_url;
let record_id = inputConfig.record_id;
let table = base.getTable("aarontable1");

let response = await fetch(fantastic_engine_url, {
    method: 'POST',
    body: JSON.stringify({
        'product_url' : product_url,
        'profile' : {
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

let output = await response.json();
await table.updateRecordAsync(record_id, {
    "subtotal": output.subtotal,
    "shipping" : output.shipping,
    "total" : output.total
});


