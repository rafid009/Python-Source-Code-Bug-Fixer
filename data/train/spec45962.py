import numpy as np 

def function(x):

	p6 = x
	k9 = 7
	paths = []
	try:
		if p6 < 6:
			p6 = k9+4
			paths.append(1)
		else:
			x = x+9
			paths.append(2)
		if k9 < 8:
			p6 = p6-7
			paths.append(3)
		else:
			x = x/k9
			p6 = p6+9
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		k9 = p6**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))