#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Hindi Wikipedia Typo Finder Bot
Author: puspaaamm
Description: This bot scans Hindi Wikipedia articles for common spelling and 
             matra (diacritic) mistakes, then generates a report. 
             It does NOT make any automatic edits (100% safe).
"""

import pywikibot
from pywikibot import pagegenerators
import re

# 1. Matra aur Spelling ki common galtiyon ka database
# Format: { r'galat_pattern': 'sahi_shabd' }
MATRA_RULES = {
    # Chhoti 'i' aur Badi 'ee' ki galtiyan
    r'\bआशिर्वाद\b': 'आशीर्वाद',
    r'\bतिथी\b': 'तिथि',
    r'\bकविन्द्र\b': 'कवींद्र',
    r'\bश्रीमति\b': 'श्रीमती',
    r'\bकवित्री\b': 'कवयित्री',
    
    # Chhota 'u' aur Bada 'oo' ki galtiyan
    r'\bसुरज\b': 'सूरज',
    r'\bप्रभू\b': 'प्रभु',
    r'\bसिन्धु\b': 'सिंधु',
    r'\bउज्वल\b': 'उज्ज्वल',
    
    # Ri (ऋ) aur R (रि) ki galtiyan
    r'\bरिषि\b': 'ऋषि',
    r'\bस्रिष्टी\b': 'सृष्टि',
    
    # Sh (श), Shh (ष) aur S (स) ki galtiyan
    r'\bकस्त\b': 'कष्ट',
    r'\bकस्ट\b': 'कष्ट',
    r'\bबिश्वास\b': 'विश्वास',
    r'\bसंसारिक\b': 'सांसारिक'
}

def scan_for_typos(limit=50):
    """
    Hindi Wikipedia ke articles ko scan karta hai aur mili hui galtiyon ki report banata hai.
    """
    # Hindi Wikipedia se connect karein
    site = pywikibot.Site('hi', 'wikipedia')
    
    # Recent changes se generator select karein (Aap iski jagah AllpagesPageGenerator bhi use kar sakte hain)
    gen = pagegenerators.RecentChangesPageGenerator(site=site, total=limit)
    
    report = []
    print("Scanning started... Please wait...\n")
    
    for page in gen:
        # Sirf main articles ko scan karein (no Talk pages, User pages, etc.)
        if page.namespace() != 0:
            continue
            
        try:
            text = page.text
            title = page.title()
            found_issues = []
            
            # Har galti ke rule ko text mein dhoondhein
            for wrong_pattern, correct_word in MATRA_RULES.items():
                matches = re.findall(wrong_pattern, text)
                if matches:
                    # Galti ka pata lagayein aur list mein save karein
                    for match in set(matches):
                        found_issues.append(f"'{match}' -> '{correct_word}'")
            
            # Agar article mein galti milti hai toh use report mein add karein
            if found_issues:
                issue_str = ", ".join(found_issues)
                report_line = f"📄 Article: [[{title}]] | Galtiyan: {issue_str}"
                report.append(report_line)
                print(report_line) # Live terminal output for feedback
                
        except Exception as e:
            print(f"Error reading page {page.title()}: {e}")
            continue

    # Final Summary Report
    print("\n" + "="*50)
    print("FINAL REPORT SUMMARY")
    print("="*50)
    if not report:
        print("Mubarak ho! Kisi bhi scanned article mein koi galti nahi mili.")
    else:
        print(f"Total {len(report)} articles mein galtiyan mili hain:\n")
        for item in report:
            print(item)
    print("="*50)

if __name__ == '__main__':
    # Default limit 50 pages ka hai, aap ise badha bhi sakte hain (e.g., limit=100)
    scan_for_typos(limit=50)

