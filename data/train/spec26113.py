import numpy as np 

def function(x):

	v5 = x
	f3 = 1
	paths = []
	try:
		if v5 <= 4:
			x = x*8
			f3 = 2+f3
			paths.append(1)
		else:
			x = v5+9
			paths.append(2)
		if v5 >= 6:
			f3 = v5+6
			paths.append(3)
		else:
			f3 = f3/6
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		f3 = v5**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))