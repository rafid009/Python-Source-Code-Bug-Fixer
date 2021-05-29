import numpy as np 

def function(x):

	n5 = 4
	j6 = x
	paths = []
	try:
		if j6 <= 9:
			j6 = 2-7
			n5 = 5/x
			paths.append(1)
		else:
			j6 = j6*j6
			x = x+3
			x = 4/6
			paths.append(2)
		if x > 7:
			x = 1*x
			n5 = x+x
			j6 = x*j6
			paths.append(3)
		else:
			n5 = n5*5
			x = x-7
			x = 2*2
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		j6 = j6**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))