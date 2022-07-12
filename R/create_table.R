create_table <- function(data_df, 
                         rowname_col = NA,
                         fig_num = "",
                         title_text = ""){
  # random_id = random_id(n=10)
  random_id = "urban_table"
  
  basic_table = data_df %>% 
    gt(id = random_id, rowname_col = rowname_col) %>% 
    tab_options(#table.width = px(760),
      table.align = "left", 
      heading.align = "left",
      # TODO: Discuss with Comms whether border should extend across 
      # whole row at bottom or just across data cells
      table.border.top.style = "hidden",
      table.border.bottom.style = "transparent",
      heading.border.bottom.style = "hidden",
      # Need to set this to transparent so that cells_borders of the cells can display properly and 
      table_body.border.bottom.style = "transparent",
      table_body.border.top.style = "transparent",
      # column_labels.border.bottom.style = "transparent",
      column_labels.border.bottom.width = px(1),
      column_labels.border.bottom.color = "black",
      # row_group.border.top.style = "hidden",
      # Set font sizes
      heading.title.font.size = px(13),
      heading.subtitle.font.size = px(13),
      column_labels.font.size = px(13),
      table.font.size = px(13),
      source_notes.font.size = px(13),
      footnotes.font.size = px(13),
      # Set row group label and border options
      row_group.font.size = px(13),
      row_group.border.top.style = "transparent",
      row_group.border.bottom.style = "hidden",
      stub.border.style = "dashed",
    ) %>% 
    tab_header(
      title = fig_num,# "eyebrow",
      subtitle = title_text) %>%  #"Top 10 Banks (by Dollar Volume) for Community Development Lending") %>% 
    # Bold title, subtitle, and columns
    tab_style(
      style = cell_text(color = "black", weight = "bold", align = "left"),
      locations = cells_title("subtitle")
    ) %>% 
    tab_style(
      style = cell_text(color = "#696969", weight = "normal", align = "left", transform = "uppercase"),
      locations = cells_title("title")
    ) %>% 
    tab_style(
      style = cell_text(color = "black", weight = "bold", size = px(13)),
      locations = cells_column_labels(gt::everything())
    ) %>% 
    # Italicize row group and column spanner text
    tab_style(
      style = cell_text(color = "black", style = "italic", size  = px(13)),
      locations = gt::cells_row_groups()
    ) %>% 
    tab_style(
      style = cell_text(color = "black", style = "italic", size  = px(13)),
      locations = gt::cells_column_spanners()
    ) %>% 
    opt_table_font(
      font = list(
        google_font("Lato"),
        default_fonts()
      )
    ) %>% 
    # Adjust cell borders for all cells, small grey bottom border, no top border
    tab_style(
      style = list(
        cell_borders(
          sides = c("bottom"),
          color = "#d2d2d2",
          weight = px(1)
        )
      ),
      locations = list(
        cells_body(
          columns =  gt::everything()
          # rows = gt::everything()
        )
      )
    )  %>%
    tab_style(
      style = list(
        cell_borders(
          sides = c("top"),
          color = "#d2d2d2",
          weight = px(0)
        )
      ),
      locations = list(
        cells_body(
          columns =  gt::everything()
          # rows = gt::everything()
        )
      )
    )  %>%
    # Set missing value defaults
    fmt_missing(columns = gt::everything(), missing_text = "...") %>%
    # Set css for all the things we can't finetune exactly in gt, mostly t/r/b/l padding
    opt_css(
      css = str_glue("
      #{random_id} .gt_row {{
        padding: 5px 5px 5px 5px;
      }}
      #{random_id} .gt_sourcenote {{
        padding: 16px 0px 0px 0px;
      }}
      #{random_id} .gt_footnote {{
        padding: 16px 0px 0px 0px;
      }}
      #{random_id} .gt_subtitle {{
        padding: 0px 0px 2px 0px;
      }}
      #{random_id} .gt_col_heading {{
        padding: 10px 5px 10px 5px;
      }}
      #{random_id} .gt_col_headings {{
        padding: 0px 0px 0px 0px;
        border-top-width: 0px;
      }}
      #{random_id} .gt_group_heading {{
        padding: 15px 0px 0px 0px;
      }}
      #{random_id} .gt_stub {{
        border-bottom-width: 1px;
        border-bottom-style: solid;
        border-bottom-color: #d2d2d2;
        border-top-color: black;
        text-align: left;
      }}
      #{random_id} .gt_grand_summary_row {{
        border-bottom-width: 1px;
        border-top-width: 1px;
        border-bottom-style: solid;
        border-bottom-color: #d2d2d2;
        border-top-color: #d2d2d2;
      }}
      #{random_id} .gt_summary_row {{
        border-bottom-width: 1px;
        border-top-width: 1px;
        border-bottom-style: solid;
        border-bottom-color: #d2d2d2;
      }}
      #{random_id} .gt_column_spanner {{
        padding-top: 10px;
        padding-bottom: 10px;
      }}
      ") %>% as.character()
    )
  
  return(basic_table)
}

