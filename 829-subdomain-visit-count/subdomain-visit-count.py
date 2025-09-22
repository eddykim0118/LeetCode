class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count = defaultdict(int)

        for cpdomain in cpdomains:
            parts = cpdomain.split(' ')
            count = int(parts[0])
            domain = parts[1]

            domain_parts = domain.split('.')

            for i in range(len(domain_parts)):
                subdomain = '.'.join(domain_parts[i:])
                domain_count[subdomain] += count

        result = []
        for domain, count in domain_count.items():
            result.append(f"{count} {domain}")

        return result
