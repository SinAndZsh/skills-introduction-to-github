package com.example.myapplication;

import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.PopupMenu;

public class MainActivity extends AppCompatActivity {

    // 声明控件
    private Button btnRightNow;
    private Button btnMaybeLater;
    private ImageButton btnPopupMenu;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // 绑定控件
        btnRightNow = findViewById(R.id.btnRightNow);
        btnMaybeLater = findViewById(R.id.btnMaybeLater);
        btnPopupMenu = findViewById(R.id.btnPopupMenu);

        // "+"按钮点击事件（弹出菜单）
        btnPopupMenu.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                PopupMenu popupMenu = new PopupMenu(MainActivity.this, v);
                popupMenu.getMenuInflater().inflate(R.menu.popup_menu, popupMenu.getMenu());
                popupMenu.setOnMenuItemClickListener(new PopupMenu.OnMenuItemClickListener() {
                    @Override
                    public boolean onMenuItemClick(MenuItem item) {
                        // 将switch语句改为if-else语句以解决"Constant expression required"问题
                        if (item.getItemId() == R.id.menu_new_chat) {
                            Toast.makeText(MainActivity.this, "New Chat", Toast.LENGTH_SHORT).show();
                            return true;
                        } else if (item.getItemId() == R.id.menu_add_contacts) {
                            Toast.makeText(MainActivity.this, "Add Contacts", Toast.LENGTH_SHORT).show();
                            return true;
                        } else if (item.getItemId() == R.id.menu_scan) {
                            Toast.makeText(MainActivity.this, "Scan", Toast.LENGTH_SHORT).show();
                            return true;
                        } else if (item.getItemId() == R.id.menu_money) {
                            Toast.makeText(MainActivity.this, "Money", Toast.LENGTH_SHORT).show();
                            return true;
                        } else if (item.getItemId() == R.id.menu_support) {
                            Toast.makeText(MainActivity.this, "Support", Toast.LENGTH_SHORT).show();
                            return true;
                        } else {
                            return false;
                        }
                    }
                });
                popupMenu.show();
            }
        });

        // RIGHT NOW 按钮点击事件
        btnRightNow.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(MainActivity.this, "RIGHT NOW", Toast.LENGTH_SHORT).show();
            }
        });

        // MAYBE LATER 按钮点击事件
        btnMaybeLater.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(MainActivity.this, "MAYBE LATER", Toast.LENGTH_SHORT).show();
            }
        });
    }
}