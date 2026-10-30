# 3. Hospital Billing and Patient Classification System Using Python

## 1. Problem Statement

Develop a Python program for a Hospital Billing and Patient Classification System. The system calculates the total hospital bill based on consultation charges, diagnostic charges, and treatment charges.

The program applies conditional concessions depending on the patient's category. It validates billing constraints to ensure that charges are not negative and that the entered values are valid.

Finally, patients are classified according to their payment policy, such as:

- Fully Paid: Patient has paid the complete bill.
- Partially Paid: Patient has paid some amount but still has a balance.
- Unpaid: Patient has not paid any amount.

The system displays the total bill, concession amount, final payable amount, payment details, and patient classification.

## 2. Algorithm

1. Start the program.
2. Enter the patient's name and age.
3. Enter consultation charges.
4. Enter diagnostic charges.
5. Enter treatment charges.
6. Validate all charges. If any charge is negative, display an error.
7. Calculate the total bill by adding all three charges.
8. Check the patient's category.
   - If the patient is a senior citizen (age 60 or above), apply a 10% concession.
   - Otherwise, if the total bill is above ₹10,000, apply a 5% concession.
   - Otherwise, no concession is applied.
9. Calculate the final payable amount.
10. Enter the amount paid by the patient.
11. Validate the payment amount.
12. Classify the patient:
    - If payment equals the final bill, classify as Fully Paid.
    - If payment is greater than zero but less than the final bill, classify as Partially Paid.
    - If payment is zero, classify as Unpaid.
13. Calculate the remaining balance.
14. Display the complete billing details.
15. Stop the program.

## 3. Flowchart (Mermaid)

\#chatgpt-mermaid-\_r_bp\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_bp\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_bp\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_bp\_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-\_r_bp\_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_bp\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_bp\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_bp\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_bp\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_bp\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_bp\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_bp\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_bp\_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_bp\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_bp\_ p{margin:0;}#chatgpt-mermaid-\_r_bp\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_bp\_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_bp\_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_bp\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_bp\_ .label text,#chatgpt-mermaid-\_r_bp\_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_bp\_ .node rect,#chatgpt-mermaid-\_r_bp\_ .node circle,#chatgpt-mermaid-\_r_bp\_ .node ellipse,#chatgpt-mermaid-\_r_bp\_ .node polygon,#chatgpt-mermaid-\_r_bp\_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-\_r_bp\_ .rough-node .label text,#chatgpt-mermaid-\_r_bp\_ .node .label text,#chatgpt-mermaid-\_r_bp\_ .image-shape .label,#chatgpt-mermaid-\_r_bp\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_bp\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_bp\_ .rough-node .label,#chatgpt-mermaid-\_r_bp\_ .node .label,#chatgpt-mermaid-\_r_bp\_ .image-shape .label,#chatgpt-mermaid-\_r_bp\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_bp\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_bp\_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_bp\_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_bp\_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-\_r_bp\_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-\_r_bp\_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_bp\_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_bp\_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_bp\_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-\_r_bp\_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_bp\_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_bp\_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_bp\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_bp\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-\_r_bp\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_bp\_ .icon-shape,#chatgpt-mermaid-\_r_bp\_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-\_r_bp\_ .icon-shape p,#chatgpt-mermaid-\_r_bp\_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-\_r_bp\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_bp\_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-\_r_bp\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_bp\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_bp\_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-\_r_bp\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_bp\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_bp\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_bp\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_bp\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_bp\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_bp\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_bp\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_bp\_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-\_r_bp\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_bp\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_bp\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_bp\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_bp\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_bp\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_bp\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_bp\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_bp\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-\_r_bp\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_bp\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_bp\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-\_r_bp\_ .node rect,#chatgpt-mermaid-\_r_bp\_ .node circle,#chatgpt-mermaid-\_r_bp\_ .node ellipse,#chatgpt-mermaid-\_r_bp\_ .node polygon,#chatgpt-mermaid-\_r_bp\_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_bp\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_bp\_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_bp\_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_bp\_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-\_r_bp\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter patient name and ageEnter consultation chargesEnter diagnostic chargesEnter treatment chargesAre all charges non-negative?Display Invalid ChargesStopCalculate Total BillAge = 60?Apply 10% ConcessionTotal Bill 10000?Apply 5% ConcessionNo ConcessionCalculate Final Payable AmountEnter Amount PaidIs Payment Valid?Display Invalid PaymentAmount Paid = Final Bill?Fully PaidAmount Paid 0?Partially PaidUnpaidCalculate BalanceDisplay Billing DetailsNoYesYesNoYesNoNoYesYesNoYesNo

## 5. Sample Input

Patient Details

```
Enter patient name: Rahul
Enter patient age: 65
Enter consultation charges: Rs. 500
Enter diagnostic charges: Rs. 2500
Enter treatment charges: Rs. 7000
Enter amount paid: Rs. 7000
```

## 6. Sample Output

Hospital Billing System

Partially Paid

```
----------- BILL DETAILS -----------

Patient Name: Rahul
Patient Age: 65
Patient Category: Senior Citizen

Consultation Charges: Rs. 500
Diagnostic Charges: Rs. 2500
Treatment Charges: Rs. 7000

Total Bill: Rs. 10000
Concession: Rs. 1000
Final Payable Amount: Rs. 9000

========== PAYMENT SUMMARY ==========

Total Bill: Rs. 10000
Concession: Rs. 1000
Final Amount: Rs. 9000
Amount Paid: Rs. 7000
Remaining Balance: Rs. 2000

Payment Status: Partially Paid

=====================================
           THANK YOU!
=====================================
```

## 7. Explanation of Concepts Used

| Python concept         | Application                           |
| ---------------------- | ------------------------------------- |
| Variables              | Store patient details and charges     |
| Input statements       | Accept patient information            |
| Data types             | Integer, float and string             |
| Arithmetic operators   | Calculate bill and concession         |
| Conditional statements | Apply discounts and classify patients |
| Comparison operators   | Validate age, charges and payment     |
| Type conversion        | Convert input into integer and float  |
| Print statements       | Display billing details               |
