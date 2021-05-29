import numpy as np 

def function(x):

	d6 = x
	f1 = x
	paths = []
	try:
		if f1 >= 1:
			x = x/9
			f1 = f1*d6
			f1 = 5/7
			paths.append(1)
		else:
			x = x*7
			paths.append(2)
		if f1 > 7:
			x = 7+x
			x = x/3
			d6 = f1*d6
			paths.append(3)
		else:
			d6 = 5+d6
			f1 = f1/5
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		f1 = f1**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))