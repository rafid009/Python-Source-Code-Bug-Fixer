import numpy as np 

def function(x):

	u5 = x
	f6 = x
	paths = []
	try:
		if u5 > 9:
			f6 = f6-5
			paths.append(1)
		else:
			u5 = x+3
			paths.append(2)
		if f6 > 5:
			x = 2-2
			x = x/1
			x = x*0
			paths.append(3)
		else:
			f6 = f6+6
			f6 = x+f6
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		u5 = u5**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))