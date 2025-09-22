class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_dict = {}

        for cpdomain in cpdomains:
            count = int(cpdomain.split()[0])
            actual_domain = cpdomain.split()[1]
            domain_dict[actual_domain] = domain_dict.get(actual_domain, 0) + count

            for index, char in enumerate(actual_domain):
                if char == '.':
                    next_domain = actual_domain[index + 1:]
                    domain_dict[next_domain] = domain_dict.get(next_domain, 0) + count

        output = []
        for key in domain_dict.keys():
            count = str(domain_dict[key])
            output.append(count + " " + key)

        return output
