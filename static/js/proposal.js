const sections = document.querySelectorAll('.form-section');

function validateSection(section) {
    const requiredFields = section.querySelectorAll(
        'input[required], textarea[required], select[required]'
    );

    for (const field of requiredFields) {
        if (!field.checkValidity()) {
            field.reportValidity();
            return false;
        }
    }

    if (section.id === 'section-1') {
        const checked = section.querySelectorAll('input[name="format_tags"]:checked').length > 0;
        if (!checked) {
            const first = section.querySelector('input[name="format_tags"]');
            first.setCustomValidity('Please select at least one format.');
            first.reportValidity();
            return false;
        }
        section.querySelectorAll('input[name="format_tags"]')
            .forEach(cb => cb.setCustomValidity(''));
    }

    if (section.id === 'section-2') {
        const checked = section.querySelectorAll('input[name="collaboration_style"]:checked').length > 0;
        if (!checked) {
            const first = section.querySelector('input[name="collaboration_style"]');
            first.setCustomValidity('Please select at least one collaboration style.');
            first.reportValidity();
            return false;
        }
        section.querySelectorAll('input[name="collaboration_style"]')
            .forEach(cb => cb.setCustomValidity(''));
    }

    return true;
}

function showSection(sectionNumber, button = null) {
    const currentSection = button
        ? button.closest('.form-section')
        : document.querySelector('.form-section:not(.hidden)');

    if (!currentSection) return;

    const currentIndex = Number(currentSection.id.replace('section-', ''));

    if (sectionNumber > currentIndex) {
        if (!validateSection(currentSection)) return;
    }

    sections.forEach(s => s.classList.add('hidden'));
    document.getElementById(`section-${sectionNumber}`).classList.remove('hidden');
    window.scrollTo({ top: 0, behavior: 'smooth' });
}