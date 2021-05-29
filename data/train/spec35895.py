import numpy as np 

def function(x):

	j3 = 6
	k9 = x
	paths = []
	try:
		if j3 <= 6:
			k9 = k9/j3
			paths.append(1)
		else:
			x = x+x
			k9 = 9*x
			paths.append(2)
		if k9 < 0:
			x = x+9
			paths.append(3)
		else:
			k9 = 5/7
			j3 = x-k9
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		j3 = k9**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))