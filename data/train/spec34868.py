import numpy as np 

def function(x):

	b6 = 5
	j5 = x
	paths = []
	try:
		if b6 >= 1:
			b6 = x-5
			x = 6-x
			paths.append(1)
		else:
			x = 6+b6
			paths.append(2)
		if b6 > 7:
			x = b6-1
			b6 = b6*0
			j5 = 3+j5
			paths.append(3)
		else:
			x = b6/9
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		b6 = j5**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))