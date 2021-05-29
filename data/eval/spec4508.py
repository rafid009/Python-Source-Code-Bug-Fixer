import numpy as np 

def function(x):

	f8 = 1
	m6 = x
	paths = []
	try:
		if m6 <= 8:
			f8 = 0+f8
			x = 1+x
			f8 = f8/x
			paths.append(1)
		else:
			m6 = 9+m6
			m6 = f8*m6
			x = x/f8
			paths.append(2)
		if x <= 7:
			m6 = 2/m6
			m6 = x/f8
			m6 = m6-f8
			paths.append(3)
		else:
			m6 = x-m6
			x = x+0
			f8 = 0/x
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