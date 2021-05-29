import numpy as np 

def function(x):

	j4 = 7
	i9 = 3
	x = x
	paths = []
	try:
		if j4 < 0:
			j4 = j4+0
			i9 = x-i9
			paths.append(1)
		else:
			x = x+6
			i9 = 6+x
			paths.append(2)
		if j4 < 7:
			i9 = 6*2
			x = i9/i9
			j4 = x*0
			paths.append(3)
		else:
			j4 = 7-j4
			j4 = j4*6
			j4 = i9*3
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		j4 = j4**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))