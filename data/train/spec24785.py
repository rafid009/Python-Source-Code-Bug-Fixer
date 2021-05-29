import numpy as np 

def function(x):

	u3 = x
	f6 = 9
	paths = []
	try:
		if x <= 1:
			x = 6*0
			paths.append(1)
		else:
			x = x-5
			f6 = x+1
			f6 = 5+f6
			paths.append(2)
		if x >= 1:
			x = 0-x
			x = u3-x
			paths.append(3)
		else:
			f6 = x-f6
			u3 = u3+0
			u3 = f6+u3
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		f6 = u3**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))