import numpy as np 

def function(x):

	q5 = 9
	f8 = 6
	paths = []
	try:
		if q5 > 3:
			f8 = f8/q5
			q5 = q5/1
			paths.append(1)
		else:
			q5 = x+q5
			x = 0+x
			paths.append(2)
		if f8 > 5:
			x = x*3
			x = x/2
			paths.append(3)
		else:
			f8 = x*f8
			q5 = 4+q5
			x = x*7
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		f8 = f8**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))