import numpy as np 

def function(x):

	o2 = x
	f9 = 9
	paths = []
	try:
		if o2 < 4:
			o2 = 6*o2
			paths.append(1)
		else:
			f9 = 2+f9
			paths.append(2)
		if f9 <= 0:
			o2 = o2+4
			f9 = 7+f9
			f9 = f9+f9
			paths.append(3)
		else:
			x = x-f9
			f9 = o2+2
			o2 = o2-6
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		f9 = f9**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))