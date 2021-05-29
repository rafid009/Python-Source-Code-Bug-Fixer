import numpy as np 

def function(x):

	b9 = 6
	j4 = 6
	paths = []
	try:
		if x < 6:
			b9 = x-b9
			j4 = j4-5
			x = j4/b9
			paths.append(1)
		else:
			j4 = j4+j4
			b9 = b9*0
			x = x*j4
			paths.append(2)
		if j4 > 8:
			b9 = 3-x
			x = x/2
			paths.append(3)
		else:
			b9 = b9*6
			j4 = 4+0
			j4 = x+5
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