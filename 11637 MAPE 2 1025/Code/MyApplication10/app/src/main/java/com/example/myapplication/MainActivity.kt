package com.example.myapplication

import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.view.View
import android.widget.Toast
import androidx.activity.OnBackPressedCallback
import androidx.appcompat.app.AppCompatActivity
import androidx.appcompat.widget.Toolbar
import androidx.core.view.GravityCompat
import androidx.drawerlayout.widget.DrawerLayout
import androidx.fragment.app.Fragment
import com.google.android.material.navigation.NavigationView

class MainActivity : AppCompatActivity(), NavigationView.OnNavigationItemSelectedListener {
    private lateinit var drawerLayout: CustomDrawerLayout
    private lateinit var navigationView: NavigationView
    private var closeMenuItem: MenuItem? = null
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        val toolbar = findViewById<Toolbar>(R.id.toolbar)
        setSupportActionBar(toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        supportActionBar?.setHomeAsUpIndicator(R.drawable.ic_menu)
        
        drawerLayout = findViewById(R.id.drawer_layout)
        navigationView = findViewById(R.id.nav_view)
        navigationView.setNavigationItemSelectedListener(this)
        
        // 监听抽屉状态变化
        drawerLayout.addDrawerListener(object : DrawerLayout.DrawerListener {
            override fun onDrawerSlide(drawerView: View, slideOffset: Float) {
                // 抽屉滑动时的处理
            }
            
            override fun onDrawerOpened(drawerView: View) {
                // 抽屉打开时显示关闭按钮
                closeMenuItem?.isVisible = true
                supportActionBar?.setHomeAsUpIndicator(R.drawable.ic_close)
            }
            
            override fun onDrawerClosed(drawerView: View) {
                // 抽屉关闭时隐藏关闭按钮
                closeMenuItem?.isVisible = false
                supportActionBar?.setHomeAsUpIndicator(R.drawable.ic_menu)
            }
            
            override fun onDrawerStateChanged(newState: Int) {
                // 抽屉状态改变时的处理
            }
        })
        
        // 处理返回键事件
        onBackPressedDispatcher.addCallback(this, object : OnBackPressedCallback(true) {
            override fun handleOnBackPressed() {
                if (drawerLayout.isDrawerOpen(GravityCompat.START)) {
                    drawerLayout.closeDrawer(GravityCompat.START)
                } else {
                    isEnabled = false
                    onBackPressedDispatcher.onBackPressed()
                }
            }
        })
        
        // Load default fragment
        if (savedInstanceState == null) {
            loadFragment(HomeFragment())
            navigationView.setCheckedItem(R.id.nav_home)
        }
    }
    
    override fun onNavigationItemSelected(item: MenuItem): Boolean {
        val fragment: Fragment = when (item.itemId) {
            R.id.nav_home -> {
                Toast.makeText(this, "首页", Toast.LENGTH_SHORT).show()
                HomeFragment()
            }
            R.id.nav_profile -> {
                Toast.makeText(this, "个人资料", Toast.LENGTH_SHORT).show()
                ProfileFragment()
            }
            R.id.nav_settings -> {
                Toast.makeText(this, "设置", Toast.LENGTH_SHORT).show()
                SettingsFragment()
            }
            R.id.nav_qr_code -> {
                Toast.makeText(this, "二维码", Toast.LENGTH_SHORT).show()
                QrCodeFragment()
            }
            else -> HomeFragment()
        }
        
        loadFragment(fragment)
        drawerLayout.closeDrawer(GravityCompat.START)
        return true
    }
    
    // 添加菜单
    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.toolbar_menu, menu)
        closeMenuItem = menu.findItem(R.id.action_close)
        closeMenuItem?.isVisible = false // 默认隐藏关闭按钮
        return true
    }
    
    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return when (item.itemId) {
            android.R.id.home -> {
                if (drawerLayout.isDrawerOpen(GravityCompat.START)) {
                    drawerLayout.closeDrawer(GravityCompat.START)
                } else {
                    drawerLayout.openDrawer(GravityCompat.START)
                }
                true
            }
            R.id.action_close -> {
                // 关闭菜单并返回主页面（首页）
                drawerLayout.closeDrawer(GravityCompat.START)
                loadFragment(HomeFragment())
                navigationView.setCheckedItem(R.id.nav_home)
                true
            }
            else -> super.onOptionsItemSelected(item)
        }
    }
    
    private fun loadFragment(fragment: Fragment) {
        supportFragmentManager.beginTransaction()
            .replace(R.id.fragment_container, fragment)
            .commit()
    }
}