<script>
    async function sendData() {
        const dataInput = document.getElementById('dataInput');
        const data = dataInput.value.trim();

        if (!data) {
            alert("Wpisz wiadomość przed wysłaniem.");
            return;
        }

        try {
            const response = await fetch('https://flask-backend-u1sd.onrender.com/save_data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ data }),
            });

            if (response.ok) {
                dataInput.value = '';
                fetchData();
            } else {
                alert('Błąd podczas wysyłania danych.');
            }
        } catch (error) {
            console.error('Błąd połączenia:', error);
        }
    }

    async function fetchData() {
        try {
            const response = await fetch('https://flask-backend-u1sd.onrender.com/get_data');
            if (response.ok) {
                const data = await response.json();
                const receivedDataDiv = document.getElementById('receivedData');
                receivedDataDiv.innerHTML = `<p>Ostatnio odebrane: ${data.last_data || 'Brak danych'}</p>`;
            } else {
                console.error('Błąd serwera przy pobieraniu danych.');
            }
        } catch (error) {
            console.error('Błąd połączenia przy pobieraniu danych:', error);
        }
    }

    window.onload = fetchData;
</script>
