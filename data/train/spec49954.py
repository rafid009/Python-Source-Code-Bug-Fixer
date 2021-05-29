import numpy as np 

def function(x):

	q1 = x
	k9 = x
	paths = []
	try:
		if k9 > 6:
			x = 6/9
			k9 = k9/4
			k9 = x/5
			paths.append(1)
		else:
			x = x+6
			x = x+6
			x = x-4
			paths.append(2)
		if x < 3:
			k9 = 7/q1
			paths.append(3)
		else:
			k9 = k9-6
			k9 = k9*0
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