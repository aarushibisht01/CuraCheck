const questions = [
    "Do you feel an uncomfortable sensation on your skin that makes you want to scratch? (Itching)",
    "Do you notice any redness, bumps, or irritation on your skin? (Skin Rash)",
    "Do you have small, raised lumps or eruptions on your skin? (Nodal Skin Eruptions)",
    "Do you experience uncontrollable sneezing that doesn’t stop easily? (Continuous Sneezing)",
    "Are you feeling cold and shaking even in normal weather? (Shivering)",
    "Do you feel a sudden and intense coldness in your body? (Chills)",
    "Do you have pain in your joints that makes it hard to move? (Joint Pain)",
    "Are you feeling pain in your stomach or abdomen? (Stomach Pain)",
    "Do you often feel a burning sensation or discomfort in your chest after eating? (Acidity)",
    "Do you have painful or open sores on your tongue? (Ulcers on Tongue)",
    "Are your muscles becoming smaller or weaker over time? (Muscle Wasting)",
    "Have you been throwing up frequently or feeling the urge to vomit? (Vomiting)",
    "Do you feel a burning sensation when you urinate? (Burning Micturition)",
    "Have you noticed small drops of blood or spotting while urinating? (Spotting in Urination)",
    "Do you feel tired or drained even after resting? (Fatigue)",
    "Have you gained weight recently without a clear reason? (Weight Gain)",
    "Do you often feel nervous, worried, or uneasy? (Anxiety)",
    "Do your hands and feet feel unusually cold? (Cold Hands and Feet)",
    "Do you frequently experience sudden changes in your mood? (Mood Swings)",
    "Have you been losing weight recently without trying? (Weight Loss)",
    "Do you feel a sense of unease and an inability to relax? (Restlessness)",
    "Do you feel excessively tired and have no energy to do anything? (Lethargy)",
    "Do you notice unusual patches or discomfort in your throat? (Patches in Throat)",
    "Are your blood sugar levels fluctuating or hard to control? (Irregular Sugar Level)",
    "Do you have a persistent cough that won’t go away? (Cough)",
    "Are you experiencing a high body temperature? (High Fever)",
    "Do your eyes appear sunken or hollow? (Sunken Eyes)",
    "Do you find it hard to breathe or feel short of breath? (Breathlessness)",
    "Do you sweat a lot, even when you are not physically active? (Sweating)",
    "Do you feel thirsty and dehydrated often? (Dehydration)",
    "Do you experience discomfort or bloating after eating? (Indigestion)",
    "Do you have pain in your head that may feel like pressure or throbbing? (Headache)",
    "Is your skin turning yellowish? (Yellowish Skin)",
    "Is your urine darker than usual? (Dark Urine)",
    "Do you often feel like vomiting or nauseated? (Nausea)",
    "Have you lost interest in eating or noticed a reduced appetite? (Loss of Appetite)",
    "Do you feel pain or pressure behind your eyes? (Pain Behind the Eyes)",
    "Are you experiencing discomfort or pain in your back? (Back Pain)",
    "Do you have difficulty passing stools or feel constipated? (Constipation)",
    "Do you feel pain or cramps in your abdomen? (Abdominal Pain)", 
    "Do you have frequent loose stools or diarrhea? (Diarrhea)",
    "Do you have a slight fever that isn’t very high? (Mild Fever)",
    "Is your urine yellow and unusual in color? (Yellow Urine)",
    "Are the whites of your eyes turning yellow? (Yellowing of Eyes)",
    "Have you experienced sudden and severe liver problems? (Acute Liver Failure)",
    "Do you feel your body is retaining excess water or fluid? (Fluid Overload)",
    "Is your stomach abnormally swollen or bloated? (Swelling of Stomach)",
    "Do you have swollen glands or lymph nodes in your neck or other areas? (Swelled Lymph Nodes)",
    "Do you feel weak or generally unwell without a specific cause? (Malaise)",
    "Is your vision blurry or distorted? (Blurred and Distorted Vision)",
    "Are you coughing up mucus or phlegm? (Phlegm)",
    "Does your throat feel scratchy, sore, or irritated? (Throat Irritation)",
    "Do your eyes look red or bloodshot? (Redness of Eyes)",
    "Do you feel pressure or pain around your nose and forehead? (Sinus Pressure)",
    "Do you have a constantly runny nose? (Runny Nose)",
    "Do you feel congested or blocked in your nose or chest? (Congestion)",
    "Do you have chest pain, especially during breathing or coughing? (Chest Pain)",
    "Do your arms or legs feel unusually weak? (Weakness in Limbs)",
    "Do you feel like your heart is beating too fast or pounding? (Fast Heart Rate)",
    "Do you experience pain when passing stools? (Pain During Bowel Movements)",
    "Do you have pain or discomfort in your anal area? (Pain in Anal Region)",
    "Have you noticed blood in your stool? (Bloody Stool)",
    "Do you feel irritation or discomfort around your anus? (Irritation in Anus)",
    "Do you have pain or stiffness in your neck? (Neck Pain)",
    "Do you feel dizzy, lightheaded, or like the room is spinning? (Dizziness)",
    "Do you experience cramps in your muscles or abdomen? (Cramps)",
    "Do you bruise easily or have unexplained bruises on your body? (Bruising)",
    "Are you overweight or obese? (Obesity)",
    "Are your legs swollen or puffy? (Swollen Legs)",
    "Do your veins look larger and swollen, especially in your legs? (Swollen Blood Vessels)",
    "Is your face or the area around your eyes swollen? (Puffy Face and Eyes)",
    "Is your thyroid gland enlarged or swollen? (Enlarged Thyroid)",
    "Are your nails brittle and break easily? (Brittle Nails)",
    "Are your hands, feet, or other extremities swollen? (Swollen Extremities)",
    "Do you feel very hungry, even after eating? (Excessive Hunger)",
    "Do you engage in extra-marital sexual relationships? (Extra-Marital Contacts)",
    "Do your lips feel dry, cracked, or tingly? (Drying and Tingling Lips)",
    "Is your speech slurred or unclear? (Slurred Speech)",
    "Do you have pain or discomfort in your knees? (Knee Pain)",
    "Do you feel pain in your hip joints? (Hip Joint Pain)",
    "Do your muscles feel weak or less strong than usual? (Muscle Weakness)",
    "Is your neck stiff or hard to move? (Stiff Neck)",
    "Do you have swelling in any of your joints? (Swelling Joints)",
    "Do you feel stiffness or difficulty in moving your body? (Movement Stiffness)",
    "Do you experience spinning sensations or feel like the room is rotating? (Spinning Movements)",
    "Do you lose balance while standing or walking? (Loss of Balance)",
    "Do you feel unstable or wobbly when walking? (Unsteadiness)",
    "Do you have weakness or difficulty moving one side of your body? (Weakness of One Body Side)",
    "Have you lost your sense of smell? (Loss of Smell)",
    "Do you feel discomfort or pain in your bladder? (Bladder Discomfort)",
    "Does your urine have a strong or foul smell? (Foul Smell of Urine)",
    "Do you feel like you need to urinate all the time? (Continuous Feeling of Urine)",
    "Do you often pass excessive gas or feel bloated? (Passage of Gases)",
    "Do you feel itching inside your body? (Internal Itching)",
    "Do you have a toxic, sick appearance like typhoid symptoms? (Toxic Look [Typhoid])",
    "Do you feel low or hopeless? (Depression)",
    "Do you feel irritable or easily annoyed? (Irritability)",
    "Do you feel pain or soreness in your muscles? (Muscle Pain)",
    "Do you feel confused or have altered consciousness? (Altered Sensorium)",
    "Do you have red spots on your skin? (Red Spots Over Body)",
    "Do you feel pain in your belly or lower abdomen? (Belly Pain)",
    "Is your menstrual cycle abnormal or irregular? (Abnormal Menstruation)",
    "Do you have discolored or patchy skin? (Dischromic Patches)",
    "Do your eyes water frequently? (Watering from Eyes)",
    "Have you felt unusually hungry recently? (Increased Appetite)",
    "Do you urinate more often than usual? (Polyuria)",
    "Do you have a family history of medical conditions? (Family History)",
    "Are you coughing up a thick, slimy substance? (Mucoid Sputum)",
    "Do you cough up rust-colored mucus? (Rusty Sputum)",
    "Do you have difficulty focusing or concentrating? (Lack of Concentration)",
    "Do you experience issues with your vision? (Visual Disturbances)",
    "Have you received a blood transfusion recently? (Receiving Blood Transfusion)",
    "Have you had unsterile injections recently? (Receiving Unsterile Injections)",
    "Have you been unconscious or in a coma? (Coma)",
    "Have you noticed blood in your vomit or stool, indicating bleeding in your stomach? (Stomach Bleeding)",
    "Do you feel a sense of fullness or tightness in your abdomen? (Distention of Abdomen)",
    "Do you have a history of consuming excessive amounts of alcohol? (History of Alcohol Consumption)",
    "Do you feel your body is retaining excess water or fluid? (Fluid Overload)",
    "Have you coughed up blood or noticed blood in your mucus? (Blood in Sputum)",
    "Do you have prominent, swollen veins on your calves or legs? (Prominent Veins on Calf)",
    "Do you feel your heart beating unusually fast, hard, or irregularly? (Palpitations)",
    "Do you experience pain in your legs or feet while walking? (Painful Walking)",
    "Do you have pimples filled with pus on your skin? (Pus-Filled Pimples)",
    "Do you notice small, dark spots or clogged pores on your skin? (Blackheads)",
    "Do you have scabs or crusts forming on your skin? (Scarring)",
    "Is your skin peeling or flaking off in patches? (Skin Peeling)",
    "Do you notice silvery scales or flakes on your skin? (Silver-Like Dusting)",
    "Do you have small, shallow dents or pits on your nails? (Small Dents in Nails)",
    "Are your nails swollen, inflamed, or painful? (Inflammatory Nails)",
    "Do you have fluid-filled blisters on your skin? (Blister)",
    "Do you have red, painful sores around your nose? (Red Sore Around Nose)",
    "Have you noticed a yellowish crust or oozing on your skin? (Yellow Crust Oozing)"
];

let currentQuestion = 0;
const answers = [];

const questionText = document.getElementById("question");
const form = document.getElementById("healthForm");
const submitBtn = document.getElementById("submitBtn");

function showQuestion(index) {
    questionText.textContent = questions[index];

    const inputs = document.querySelectorAll('input[name="answer"]');

    
    inputs.forEach(input => {
        input.checked = false;
    });

   
    if (answers[index] !== undefined) {
        const selected = document.querySelector(`input[name="answer"][value="${answers[index]}"]`);
        if (selected) selected.checked = true;
    }

  
    submitBtn.style.display = index === questions.length - 1 ? "inline-block" : "none";
}


showQuestion(currentQuestion);

function nextQuestion() {
    const selected = document.querySelector('input[name="answer"]:checked');
    if (!selected) {
    alert("Please select an answer.");
    return;
    }
    answers[currentQuestion] = parseInt(selected.value);
    currentQuestion++;
    if (currentQuestion < questions.length) {
    showQuestion(currentQuestion);
    }
}

function prevQuestion() {
    if (currentQuestion > 0) {
    currentQuestion--;
    showQuestion(currentQuestion);
    }
}

form.addEventListener("submit", function (e) {
    e.preventDefault();
    const selected = document.querySelector('input[name="answer"]:checked');
    if (!selected) {
        alert("Please select an answer.");
        return;
    }
    answers[currentQuestion] = parseInt(selected.value);
    console.log("Submitted Answers:", answers);
    alert("Form submitted! Data logged in console.");
});
function smoothScrollToChecker() {
  const section = document.getElementById("checker");
  section.scrollIntoView({ behavior: "smooth" });
}

showQuestion(currentQuestion);