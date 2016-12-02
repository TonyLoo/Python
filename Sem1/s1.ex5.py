#corect
sir="de	unde si cum 	"

def gaseste(sir):
	for c in sir:
		if c in '\r\t\n\a\b\f\v':
			return True
	return False

print gaseste(sir)

