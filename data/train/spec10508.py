import numpy as np 

def function(x):

	k9 = 5
	d2 = x
	paths = []
	try:
		if x <= 6:
			x = d2/7
			paths.append(1)
		else:
			k9 = 3*k9
			k9 = 9*k9
			x = x/2
			paths.append(2)
		if d2 < 5:
			k9 = k9*0
			k9 = 2-k9
			paths.append(3)
		else:
			x = 4+4
			k9 = d2-k9
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		k9 = k9**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))