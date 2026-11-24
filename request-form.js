(() => {
    const form = document.getElementById('request-form');
    if (!form) return;

    form.addEventListener('submit', (event) => {
        event.preventDefault();
        if (!form.reportValidity()) return;
        const submitButton = form.querySelector('[type="submit"]');
        if (submitButton) submitButton.disabled = true;

        const data = new FormData(form);
        const model = String(data.get('model') || '').trim();
        const service = String(data.get('service') || '').trim();
        const details = String(data.get('details') || '').trim();
        const message = [
            'Olá! Gostaria de solicitar uma avaliação.',
            `Modelo do aparelho: ${model}`,
            `Serviço: ${service}`,
            `Descrição do problema: ${details}`,
            '',
            'Não vou enviar senhas, PINs nem códigos de verificação.'
        ].join('\n');
        const whatsappUrl = `https://wa.me/5511939432371?text=${encodeURIComponent(message)}`;
        const whatsappWindow = window.open(whatsappUrl, '_blank', 'noopener,noreferrer');
        if (!whatsappWindow) {
            window.location.href = whatsappUrl;
            return;
        }
        if (submitButton) submitButton.disabled = false;
    });
})();
