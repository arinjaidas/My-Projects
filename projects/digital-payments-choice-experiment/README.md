# Digital Payments and Default-Choice Experiment

A public synthetic demonstration of a behavioural-economics workflow motivated by the documented GIPE group project on payment defaults and switching friction.

## Runnable demonstration

The code generates fictional responses, compares group choice shares, estimates an HC3 linear probability model and logistic regression, and reports the average discrete change in predicted payment choice.

![Synthetic demonstration](demo_output/choice.svg)

```bash
python -m pip install -r requirements.txt
python -m unittest -v test_demo.py
python demo.py --demo --output demo_output
```

All bundled response records and estimates are synthetic. They are not original study findings. The public workflow keeps only its explicit analysis fields and exports aggregate/model outputs.

## Project context

The original academic project developed a two-form survey comparing active choice with UPI preselection, with empirical analysis and robustness work. Arinjai Das contributed to quantitative analysis and interpretation within Group 8 at GIPE.

The recovered original research scripts and historical result files are not part of this public edition. Their publication is pending explicit sharing approval after upload review identified possible unpublished institutional material.

## Attribution

The academic paper lists Aayushika Bhardwaj, Shreya Bhardwaj, Adhya Pande, Kunal Sachdeva, Bipasha and Arinjai Das. This synthetic demonstration was newly implemented in October 2026 with ChatGPT assistance.
