import numpy as np 

def function(x):

	k9 = 3
	j8 = 8
	x = 2
	paths = []
	try:
		if j8 > 2:
			k9 = 1+k9
			k9 = k9-5
			paths.append(1)
		else:
			j8 = x*j8
			j8 = 4-j8
			x = x/j8
			paths.append(2)
		if k9 >= 9:
			j8 = j8/k9
			j8 = j8/j8
			paths.append(3)
		else:
			x = 4+x
			j8 = j8-2
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		j8 = k9**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))