import numpy as np 

def function(x):

	q5 = 8
	i8 = x
	paths = []
	try:
		if i8 >= 5:
			q5 = q5+8
			q5 = i8-7
			q5 = 6/q5
			paths.append(1)
		else:
			x = x*3
			x = 5/i8
			q5 = q5-i8
			paths.append(2)
		if x <= 4:
			q5 = x-1
			paths.append(3)
		else:
			x = 9-9
			i8 = x*0
			x = x-4
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		x = i8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))