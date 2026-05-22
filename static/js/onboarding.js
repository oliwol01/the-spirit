const steps = document.querySelectorAll('.onboarding-step');

let currentStep = 0;

function showStep(index) {

  steps.forEach((step, i) => {

    step.style.display = i === index ? 'block' : 'none';

  });

}

showStep(currentStep);

document.addEventListener('click', (e) => {

  if (e.target.matches('.btn-next')) {

    const currentInputs = steps[currentStep].querySelectorAll(
      'input[required], textarea[required], select[required]'
    );

    let valid = true;

    currentInputs.forEach(input => {

      if (!input.checkValidity()) {

        input.reportValidity();

        valid = false;

      }

    });

    if (valid && currentStep < steps.length - 1) {

      currentStep++;

      showStep(currentStep);

    }

  }

  if (e.target.matches('.btn-back')) {

    if (currentStep > 0) {

      currentStep--;

      showStep(currentStep);

    }

  }

});