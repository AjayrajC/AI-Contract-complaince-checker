import os
import sys
from src.compliance_rules import check_compliance
from src.text_extraction import extract_text

# Path to the contract file
CONTRACT_FILE_PATH = "path/to/contract.pdf"

# Main function to run the compliance checker
def main():
    try:
        # Step 1: Extract text from the contract
        print("Extracting text from the contract...")
        contract_text = extract_text(CONTRACT_FILE_PATH)
        if not contract_text:
            print("Failed to extract text from the contract.")
            sys.exit(1)

        # Step 2: Run compliance checks
        print("Running compliance checks...")
        compliance_results = check_compliance(contract_text)

        # Step 3: Display or save the results
        print("\nCompliance Check Results:")
        for rule, result in compliance_results.items():
            status = "Pass" if result else "Fail"
            print(f"{rule}: {status}")

        # Optional: Save results to a file
        results_file = "compliance_results.txt"
        with open(results_file, "w") as f:
            for rule, result in compliance_results.items():
                status = "Pass" if result else "Fail"
                f.write(f"{rule}: {status}\n")
        print(f"Results saved to {results_file}")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
