import numpy as np 

def function(x):

	v3 = 3
	k9 = x
	x = x
	paths = []
	try:
		if x < 3:
			k9 = k9-k9
			paths.append(1)
		else:
			k9 = v3-k9
			v3 = 5*0
			paths.append(2)
		if k9 >= 4:
			x = 5-9
			x = k9*3
			paths.append(3)
		else:
			x = x*4
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