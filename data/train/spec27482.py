import numpy as np 

def function(x):

	p3 = x
	k9 = x
	paths = []
	try:
		if x <= 5:
			x = 8*2
			paths.append(1)
		else:
			k9 = p3-k9
			paths.append(2)
		if x < 5:
			k9 = 8-k9
			k9 = 1-k9
			p3 = 8-p3
			paths.append(3)
		else:
			p3 = p3*2
			x = x/x
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		k9 = p3**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))