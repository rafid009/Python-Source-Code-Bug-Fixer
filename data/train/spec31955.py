import numpy as np 

def function(x):

	f2 = 9
	m5 = x
	paths = []
	try:
		if m5 < 1:
			x = x+4
			m5 = x/m5
			paths.append(1)
		else:
			x = x*6
			x = x+x
			f2 = f2-4
			paths.append(2)
		if f2 >= 3:
			f2 = f2-m5
			f2 = f2+5
			paths.append(3)
		else:
			f2 = m5*4
			x = x/9
			f2 = 8/7
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		m5 = f2**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))