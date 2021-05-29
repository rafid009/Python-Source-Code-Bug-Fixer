import numpy as np 

def function(x):

	j5 = 4
	q4 = x
	x = 2
	paths = []
	try:
		if x < 7:
			x = x+x
			j5 = q4*7
			j5 = 8*6
			paths.append(1)
		else:
			q4 = q4*x
			paths.append(2)
		if j5 <= 7:
			q4 = 2+q4
			paths.append(3)
		else:
			j5 = q4-7
			j5 = j5*4
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		j5 = j5**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))