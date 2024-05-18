// Przykład pseudokodu dla Node.js z użyciem biblioteki Kue do kolejkowania zapytań

const kue = require('kue');
const app = kue.createQueue();

// Frontend wysyła żądanie
app.post('/api/data', (req, res) => {
    // Tworzenie zadania w kolejce
    const job = app.create('process_data', {
        title: 'Processing data from frontend',
        data: req.body.data
    }).save((err) => {
        if (err) res.status(500).send('Error queuing the request');
        res.status(202).send('Request queued');
    });

    // Przetwarzanie zadania
    job.on('complete', (result) => {
        console.log('Job completed with data ', result);
    }).on('failed', (errorMessage) => {
        console.log('Job failed');
    });
});

// Przetwarzanie żądań w kolejce
app.process('process_data', (job, done) => {
    processData(job.data);
    done();
});

function processData(data) {
    // Logika przetwarzania danych
}
