import numpy as np 

def function(x):

	j5 = 0
	i5 = x
	paths = []
	try:
		if j5 > 9:
			j5 = 3+j5
			paths.append(1)
		else:
			j5 = i5*0
			x = 3+0
			paths.append(2)
		if x < 4:
			x = x/i5
			x = x*5
			j5 = 7/3
			paths.append(3)
		else:
			j5 = j5*x
			j5 = 4+i5
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		i5 = i5**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))